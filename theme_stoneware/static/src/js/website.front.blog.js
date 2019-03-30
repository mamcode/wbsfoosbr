odoo.define('theme_stoneware.front_js_blog',function(require){
    'use strict';

var utils = require('web.utils');
var sAnimation = require('website.content.snippets.animation');

sAnimation.registry.latest_blog = sAnimation.Class.extend({
    selector : ".web_blog_slider",
    start: function () {
        var self = this;
        if(this.editableMode){
          self.$target.empty().append('<div class="seaction-head"><h1>Blog SLider</h1></div>'); 
        }
        if (!this.editableMode) {
            var list_id=self.$target.attr('data-blog_list-id') || false;
            $.get("/blog/get_blog_content",{'blog_config_id':list_id}).then(function (data){
        if(data){
            self.$target.empty().append(data);
            self.$target.removeClass("hidden");
        }});
        }
    },
});
});

