import csv
import io
import urllib
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .forms import CSVUploadForm
from .models import Post

class Index(generic.ListView):
    """
    役職テーブルの一覧表作成
    """
    model = Post
    template_name = 'csvdownload/list.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_name'] = 'csvdownload'
        return ctx

class PostImport(generic.FormView):
    """
    役職テーブルの登録(csvアップロード)
    """
    template_name = 'csvdownload/import.html'
    success_url = reverse_lazy('csvdownload:index')
    form_class = CSVUploadForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['form_name'] = 'csvdownload'
        return ctx

    def form_valid(self, form):
        """postされたCSVファイルを読み込み、役職テーブルに登録します"""
        csvfile = io.TextIOWrapper(form.cleaned_data['file'])
        reader = csv.reader(csvfile)
        for row in reader:
            """
            役職テーブルを役職コード(primary key)で検索します
            """
            post, created = Post.objects.get_or_create(pk=row[0])
            post.name = row[1]
            post.save()
        return super().form_valid(form)

def PostExport(request):
    """
    役職テーブルを全件検索して、CSVファイルを作成してresponseに出力します。
    """
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'CSVファイル.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)
    for post in Post.objects.all():
        writer.writerow([post.pk, post.name])
    return response
