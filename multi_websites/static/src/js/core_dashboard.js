odoo.define('multi_websites.backend', function (require) {
"use strict";
/* Copyright (c) 2016-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>) */
    /* See LICENSE file for full copyright and licensing details. */
var WebsiteBackend = require('website.backend.dashboard');
var core = require('web.core');
var QWeb = core.qweb;
WebsiteBackend.include({
   
    update_cp: function() {
        var self = this;
        if (!this.$searchview) {
            this.$searchview = $(QWeb.render("website.DateRangeButtons", {
                widget: this,
            }));
            this.$searchview.change('.wk_multi_website_dashboard', function(ev) {
                var website_id  = $(this).val()
                console.log($(this).val());
                self._rpc({
                route: '/set/multiwebsite/id',
                    params: {
                        website_id: website_id,
                    },
                }).done(function(result) {
                    // Change the sales. 
                     self.on_date_range_button('week');
                });
               
            });
            this.$searchview.click('button.js_date_range', function(ev) {
                self.on_date_range_button($(ev.target).data('date'));
                $(this).find('button.js_date_range.active').removeClass('active');
                $(ev.target).addClass('active');
            });
        }
        self.update_control_panel({
            cp_content: {
                $searchview: this.$searchview,
                
            },
            breadcrumbs: self.getParent().get_breadcrumbs(),
        });

    },
});
});
