odoo.define('theme_stoneware.editor_js',function(require) {
'use strict';
    var ajax = require('web.ajax');
    var core = require('web.core');
    var ajax = require('web.ajax');
    var core = require('web.core');
    var rpc = require('web.rpc');
    var weContext = require('web_editor.context');
    var web_editor = require('web_editor.editor');
    var options = require('web_editor.snippets.options');
    var wUtils = require('website.utils');
    var qweb = core.qweb;
    var _t = core._t;
    ajax.loadXML('/theme_stoneware/static/src/xml/change_progress.xml', core.qweb);
    ajax.loadXML('/theme_stoneware/static/src/xml/product_template.xml', core.qweb);


    var advance_product_slider_common = options.Class.extend({
    		popup_template_id: "editor_new_product_slider_template",
    		popup_title: _t("Select Collection"),
            product_slider_configure: function(type,value) {
                var self = this;
                var def = wUtils.prompt({
                    'id': this.popup_template_id,
                    'window_title': this.popup_title,
                    'select': _t("Collection"),
                    'init': function (field) {
                        return rpc.query({
                                model: 'multitab.configure',
                                method: 'name_search',
                                args: ['', []],
                                context: weContext.get(),
                            });
                    },
                });            
                def.then(function (collection_id) {
                    self.$target.attr("data-tab-id", collection_id);
                    ajax.jsonRpc('/web/dataset/call', 'call', {
                        model: 'multitab.configure',
                        method: 'read',
                        args: [[parseInt(collection_id)], ['name'], weContext.get()],
                    }).then(function (data) {
                      if(data && data[0] && data[0].name)
                        self.$target.empty().append('<div class="container"><div class="advance_product_slider"><div class="col-md-12"><div class="seaction-head"><h1>'+ data[0].name +'</h1> </div></div></div></div>');   
                         
                    });
                    
                });
                return def;
            },
            onBuilt: function () {
                var self = this;
                this._super();
                this.product_slider_configure('click').fail(function () {
                self.getParent()._onRemoveClick($.Event( "click" ));            	       	
                });
            }
        });

    options.registry.advance_product_slider = advance_product_slider_common.extend({        
        cleanForSave: function(){
        this.$target.addClass("hidden");
        }
    });

	options.registry.tabslide = options.Class.extend({
        start : function () {
            var self = this;
            this.id = this.$target.attr("id");
            this.$inner = this.$target.find("div[class='tab-content']");
            this.$indicators = this.$target.find("ul[role='tablist']");
            return this._super.apply(this, arguments);
        },   	
        add_tab: function(type,value) {
            var self = this;
    		var cycle = this.$inner.length;
    		var id=new Date().getTime();
    		this.$indicators.append('<li role="presentation"><a href="#'+id+'" aria-controls="profile" role="tab" data-toggle="tab">New Tab</a></li>');
			this.$inner.append('<div role="tabpanel" class="tab-pane" id="'+id+'">Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </div>')
		},
        remove_tab: function(type,value){
            var self = this;
    		var cycle = this.$inner.length;
            
            if(this.$inner.find("div[class='tabpanel'].active").first()){
    		var $active_tab = this.$inner.find("div[class='tabpanel'].active").first();
    		var $active_content=this.$indicators.find('li.active').first();
    		$active_tab.remove();
            $active_content.remove();
           }
           return;
        },
        onBuilt: function() {
            this.id = "tab_slide_" + new Date().getTime();
            this.$target.attr("id", this.id);    
        },
    });

    options.registry.theme_progressbar = options.Class.extend({
    start : function () {
        var self = this;
        this.id = this.$target.attr("id");
    },      
    change_progress: function(type,value) {
        var self = this;
        if(type == 'reset'){
        self.$modal = $(qweb.render("theme_stoneware.change_progress_modal"));
        self.$modal.appendTo('body');
        self.$modal.modal();
        var $progress_width = self.$modal.find("#progress-width"),
        $sub_data = self.$modal.find("#sub_data");                                                          
        $sub_data.on('click', function() {
        self.$target.attr('data-animate-width',$progress_width.val()+'%');
        self.$target.attr('style','width:'+$progress_width.val()+'%;');   
        });
        }         
        
            return;
        },
    });
    options.registry.product_brand_slider = options.Class.extend({

        brand_slider_configure: function(type,value) {
            var self = this;
            if(type == false || type == 'click'){
                self.$modal = $(qweb.render("theme_stoneware.brand_slider_block"));
                self.$modal.appendTo('body');
                self.$modal.modal();
                var $brand_count = self.$modal.find("#brand-count"),
                    $cancel = self.$modal.find("#cancel"),
                    $sub_data = self.$modal.find("#sub_data"),
                    $brand_label = self.$modal.find("#brand-label");                           
                    $sub_data.on('click', function() {
                        var type = '';
                        self.$target.attr("data-brand-count", $brand_count.val());
                        if ($brand_label.val()) {
                            type = $brand_label.val();
                        } 
                        else {
                            type = "Brands";
                        }
                        self.$target.attr("data-brand-label", type);
                        self.$target.empty().append('<div class="container"><div class="shopper_brand_slider"><div class="col-md-12"><div class="seaction-head"><h1>' + type + '</h1> </div></div></div></div>');
                    });
            }                
            return;
        },
        onBuilt: function () {
            var self = this;
            this._super();
            this.brand_slider_configure("click").fail(function () {
                self.getParent()._removeSnippet();
            });
        },
        cleanForSave: function(){
            this.$target.empty();
        }
    });
});


