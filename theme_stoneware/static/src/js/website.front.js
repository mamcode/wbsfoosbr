odoo.define('theme_stoneware.front_js',function(require){
	'use strict';
  var sAnimation = require('website.content.snippets.animation');
  
  function initialize_owl(el){
   el.owlCarousel({
    items: 4,
            margin: 30,
            navigation: true,
            pagination: false,
            responsive: {
                0: {
                    items: 1,
                },
                481: {
                    items: 2,
                },
                768: {
                    items: 3,
                },
                1024: {
                    items: 4,
                }
            }

   });
  }
  function destory_owl(el){
    if(el && el.data('owlCarousel'))
   {
    el.data('owlCarousel').destroy();
    el.find('.owl-stage-outer').children().unwrap();
    el.removeData();
    }
  }
  sAnimation.registry.advance_product_slider = sAnimation.Class.extend({
    selector : ".tqt_products_slider",
        start: function (editMode) {
            var self = this;
			if (self.editableMode)
            {
             self.$target.empty().append('<div class="container"><div class="advance_product_slider"><div class="col-md-12"><div class="seaction-head"><h1>Product Slider</h1> </div></div></div></div>');
			}
			if(!self.editableMode){
			var	tab_collection=parseInt(self.$target.attr('data-tab-id') || 0),
				slider_id='tqt_products_slider'+new Date().getTime();

            $.get("/shop/get_products_content",{'tab_id':self.$target.attr('data-tab-id') || 0,
												'slider_id':slider_id,

            									}).then(function( data ) {
                if(data){                   
                    self.$target.empty().append(data);
					$(".tqt_products_slider").removeClass('hidden');
					initialize_owl($(".tqt-pro-slide"));
    				
                }
            });
			}
        }
    });

    sAnimation.registry.product_brand_slider = sAnimation.Class.extend({
        selector: ".tqt_product_brand_slider",
        start: function(editable_mode) {
            var self = this;
            if (self.editableMode) {
                self.$target.empty().append('<div class="container"><div class="shopper_brand_slider"><div class="col-md-12"><div class="seaction-head"><h1>Brand Slider</h1> </div></div></div></div>');
            }
            if (!self.editableMode) {
                $.get("/shop/get_product_brand_slider", {
                    'label': self.$target.attr('data-brand-label') || '',
                    'brand-count': self.$target.attr('data-brand-count') || 0,
                }).then(function(data) {
                    if (data) {
                        self.$target.empty().append(data);
    					$(".tqt_product_brand_slider").removeClass('hidden');
    					$.getScript("/theme_stoneware/static/src/js/owl.carousel.min.js");
                        self.$target.find("#as_our_brand").owlCarousel({
                            items: parseInt(self.$target.attr('data-brand-count')) || 8,
                            margin: 10,
                            navigation: true,
                            pagination: false,
                            responsive: {
                                0: {
                                    items: 2,
                                },
                                481: {
                                    items: 3,
                                },
                                768: {
                                    items: 4,
                                },
                                1024: {
                                    items: parseInt(self.$target.attr('data-brand-count')) || 8,
                                }
                            }
                        });
					}
				});
			}
}
	});

    sAnimation.registry.accordion_option1 = sAnimation.Class.extend({
        selector: ".accordion-option1",
        start: function(editable_mode) {
            var self = this;
            if(!editable_mode){
                self.$target.find("div.panel-heading").addClass("collapsed");
                self.$target.find("div.panel-collapse").addClass("collapse").removeClass("in");
            }
        }
    });

    sAnimation.registry.accordion_option2 = sAnimation.Class.extend({
        selector: ".accordion-option2",
        start: function(editable_mode) {
            var self = this;
            if(!editable_mode){
                self.$target.find("div.panel-heading").addClass("collapsed");
                self.$target.find("div.panel-collapse").addClass("collapse").removeClass("in");
            }
        }
    });

    sAnimation.registry.accordion_option3 = sAnimation.Class.extend({
        selector: ".accordion-option3",
        start: function(editable_mode) {
            var self = this;
            if(!editable_mode){
                self.$target.find("div.panel-heading").addClass("collapsed");
                self.$target.find("div.panel-collapse").addClass("collapse").removeClass("in");
            }
        }
    });
	sAnimation.registry.contactus = sAnimation.Class.extend({
		selector : ".as-contact-us-m",
		start: function () {
		    var self = this;
		this.$target.find("input[name='csrf_token']").replaceWith('<input type="hidden" name="csrf_token" t-att-value="csrf_token  or request.csrf_token()"/>');       
		},
	});
	sAnimation.registry.contactus_1 = sAnimation.Class.extend({
		selector : ".as-get-in-touch",
		start: function () {
		    var self = this;
		this.$target.find("input[name='csrf_token']").replaceWith('<input type="hidden" name="csrf_token" t-att-value="csrf_token  or request.csrf_token()"/>');       
		},
	});
	sAnimation.registry.contactus_1 = sAnimation.Class.extend({
		selector : ".as-contact-us",
		start: function () {
		    var self = this;
		this.$target.find("input[name='csrf_token']").replaceWith('<input type="hidden" name="csrf_token" t-att-value="csrf_token  or request.csrf_token()"/>');       
		},
	});
});

