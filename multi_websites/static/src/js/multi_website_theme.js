odoo.define('multi_websites.theme', function(require){
    "use strict";
    /* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
    /* See LICENSE file for full copyright and licensing details. */
    var WebsiteTheme = require('website.theme');
    function multi_website_theme_views () {
        return $("link[href*='multi_websites.multi_website']");
    }

    WebsiteTheme.include({
        update_style: function (enable, disable, reload) {
            var links = multi_website_theme_views();
            if (links.length) {
                links.last().after(
                    $("<link rel='fake' href='/web.assets_frontend.fake'/>")
                );
            }
            return this._super.apply(this, arguments).done(function () {
                links.remove();
            });
        }
    });
    return {
        multi_website_theme_views: multi_website_theme_views,
    };
});
