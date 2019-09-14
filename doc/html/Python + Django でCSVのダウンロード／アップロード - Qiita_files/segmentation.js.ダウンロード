(function () {
    'use strict';

    if (!window.FOut) window.FOut = {};

    if (!window._fout_queue) window._fout_queue = {};
    if (!window._fout_queue.segment) window._fout_queue.segment = {};
    if (!window._fout_queue.segment.queue) window._fout_queue.segment.queue = [];
    if (!window._fout_queue.segment.status) window._fout_queue.segment.status = {};
    if (!window._fout_queue.segment.status.request_count) window._fout_queue.segment.status.request_count = {};
    if (!window._fout_queue.segment.status.sent_user) window._fout_queue.segment.status.sent_user =  {};

    FOut.DMP = (function (undef) {

        var DMP = {};

        function for_each(queue, callback, max_request, request_count, sent_user) {

            var i, q;

            for (i = 0, q = queue[i]; q; q = queue[++i]) {
                var user_id = (q.user_id != undef) ? parseInt(q.user_id, 10) : 0;
                var service = (q.advertiser_id !== undef) ? 2 : 1;
                var segment_id = (q.segment_id != undef) ?
                    parseInt(q.segment_id, 10) : '';
                var event = (q.event !== undef) ? q.event : '';

                if (request_count[service] && request_count[service] >= max_request) {
                    continue;
                }

                if (user_id <= 0) {
                    continue;
                }

                var key = [user_id, segment_id, event].join(':');
                if (sent_user[key]) {
                    continue;
                }

                var res = callback(q);

                if (res) {
                    if (!request_count[service]) {
                        request_count[service] = 1;
                    } else {
                        request_count[service]++;
                    }
                    if (user_id > 0) sent_user[key] = true;
                }
            }
        }

        function get_parent_url(query_params) {
            var url = '';

            if ('pageurl' in query_params && 'pageref' in query_params) {
                return decodeURIComponent(query_params.pageurl);
            }

            try {
                url = parent.document.URL;
            } catch (e) {
                url = document.referrer;
            }
            return url;
        }

        function get_referrer_url(query_params) {
            var url = '';

            if ('pageurl' in query_params && 'pageref' in query_params) {
                return decodeURIComponent(query_params.pageref);
            }

            try {
                url = parent.document.referrer;
            } catch (e) {
                url = '';
            }
            return url;
        }

        function check_mobile_safari() {
            var useragents = [ 'iPhone', 'iPod', 'iPad' ].join('|');
            var pattern = new RegExp(useragents, 'i');
            return pattern.test(navigator.userAgent);
        }

        function support_localstorage() {
            var ret = false;

            try {
                if (window.localStorage) {
                    ret = true;
                }
            } catch (e) {
            }

            return ret;
        }

        function is_valid_url(url) {
            var re = /^http/;
            return re.test(url) || url === '';
        }

        function append_iframe(src) {
            var el = document.createElement('iframe');
            el.src = src;
            el.style.display = 'none';
            wait_dom_ready(function() {
                document.body.appendChild(el);
            });
        }

        function append_script(src, is_async) {
            var el = document.createElement('script');
            el.type = 'text/javascript';
            el.async = is_async;
            el.src = src;
            var s = document.getElementsByTagName('script')[0];
            s.parentNode.insertBefore(el, s);
        }

        function wait_dom_ready(callback) {
            var is_loaded = false;

            if (document.readyState === 'complete' || document.readyState === 'loaded') {
                callback();
                return;
            }

            if (document.addEventListener){
                document.addEventListener('DOMContentLoaded',function(){
                    callback();
                    is_loaded = true;
                }, false);
                window.addEventListener('load', function(){
                    if (!is_loaded) callback();
                }, false);
            } else if (window.attachEvent) {
                if (window.ActiveXObject && window === window.top) {
                    _ie();
                } else {
                    window.attachEvent('onload', callback);
                }
            } else {
                var _onload = window.onload;
                window.onload = function(){
                    if (typeof _onload === 'function') {
                        _onload();
                    }
                    callback();
                };
            }

            function _ie(){
                try {
                    document.documentElement.doScroll('left');
                } catch (e) {
                    setTimeout(_ie, 0);
                    return;
                }
                callback();
            }
        }

        function parse_query_strings() {
            var params = window.location.search.substring(1).split('&'),
                hashes = window.location.hash.substring(1).split('&'),
                result = {},
                i, pos, key, val;

            for (i = 0; i < params.length; i++) {
                pos = params[i].indexOf('=');
                if (pos > 0) {
                    key = params[i].substring(0, pos);
                    val = params[i].substring(pos + 1);
                    result[key] = val;
                }
            }

            for (i = 0; i < hashes.length; i++) {
                pos = hashes[i].indexOf('=');
                if (pos > 0) {
                    key = hashes[i].substring(0, pos);
                    val = hashes[i].substring(pos + 1);
                    if (!(key in result)) {
                        result[key] = val;
                    }
                }
            }

            try {
                var parent_hashes = parent.window.location.hash.substring(1).split('&');
                for (i = 0; i < parent_hashes.length; i++) {
                    pos = parent_hashes[i].indexOf('=');
                    if (pos > 0) {
                        key = parent_hashes[i].substring(0, pos);
                        val = parent_hashes[i].substring(pos + 1);
                        if (!(key in result)) {
                            result[key] = val;
                        }
                    }
                }
            } catch (e) {}

            return result;
        }

        function is_array(val) {
            return Object.prototype.toString.call(val) === '[object Array]';
        }

        function _run(target, request_count, sent_user) {

            var max_request = 10,
                host = 'https://cnt.fout.jp',
                query_params = parse_query_strings(),
                url = get_parent_url(query_params),
                referrer_url = get_referrer_url(query_params);

            if (!is_valid_url(url)) return;

            for_each(target, function(q) {
                var user_id = parseInt(q.user_id, 10) || 0,
                    site_id = parseInt(q.site_id, 10) || '',
                    segment_id = parseInt(q.segment_id, 10) || '',
                    price = parseInt(q.price, 10) || '',
                    dat   = q.dat || '',
                    params = q.params || {},
                    ex_url = q.ex_url || '',
                    encoding = q.encoding || '',
                    event = q.event || '',
                    item = q.item || [],
                    category = q.category || '',
                    keywords = q.keywords || '',
                    brand = q.brand || '',
                    cv_price = q.cv_price || [],
                    cachebuster = Math.floor(Math.random() * 10e12);

                if (user_id < 800) return false;

                if (ex_url) {
                    url = ex_url;
                }

                var params_array = [];
                for (var i in params) {
                    if (params.hasOwnProperty(i)) {
                        params_array.push(i + "=" + params[i]);
                    }
                }
                var param_string = params_array.join('&');
                var item_list_string = is_array(item) ? item.join(',') : item;
                var cv_price_string = is_array(cv_price) ? cv_price.join(',') : cv_price;

                var queries = [
                    'id=' + user_id,
                    'url=' + encodeURIComponent(url),
                    'rurl=' + encodeURIComponent(referrer_url),
                    'siteid=' + site_id,
                    'segid=' + segment_id,
                    'price=' + price,
                    'dat='   + encodeURIComponent(dat),
                    'params=' + encodeURIComponent(param_string),
                    'encoding=' + encodeURIComponent(encoding),
                    'event=' + event,
                    'item=' + encodeURIComponent(item_list_string),
                    'category=' + encodeURIComponent(category),
                    'keywords=' + encodeURIComponent(keywords),
                    'brand=' + encodeURIComponent(brand),
                    'cv_price=' + encodeURIComponent(cv_price_string),
                    'bc=1',
                    'cachebuster=' + cachebuster
                ];

                (new Image()).src = host + '/' + user_id + '/cnt?' + queries.join('&');

                return true;
            }, max_request, request_count, sent_user);

        }

        DMP.run = function() {

            var fout_queue = window._fout_queue;
            var segment_queue = window._fout_queue.segment.queue;
            var segment_status = window._fout_queue.segment.status;

            _run(segment_queue, segment_status.request_count, segment_status.sent_user);

            var is_mobile_safari = check_mobile_safari() && support_localstorage(),
                beacon_src = 'https://' + ((is_mobile_safari) ? 'dsp.fout.jp/js' : 'js.fout.jp') + '/beacon.html?from=dmp';

            if (fout_queue.nortbsync) beacon_src += '&nortbsync=1';

            if (!segment_status.is_beaconed) {
                var src = beacon_src;
                append_iframe(src);
                segment_status.is_beaconed = true;
            }

            if (fout_queue.tracker && !window._gaq) {
                append_script('https://js.fout.jp/referrer.js', true);
            }

            if (fout_queue.itpcv && fout_queue.itpcv['is_itpcv']) {
                append_script('https://js.fout.jp/itpcv.js', true);
            }

            if (fout_queue.redirect && fout_queue.redirect['is_redirect']) {
                append_script('https://js.fout.jp/redirect.js', true);
            }
        };

        DMP.execute = function (target) {

            var request_count = {};
            var sent_user = {};

            _run(target, request_count, sent_user);
        };

        return DMP;
    })();
})();
FOut.DMP.run();

