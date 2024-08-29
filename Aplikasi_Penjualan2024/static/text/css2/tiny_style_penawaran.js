//** Accordion Content script: By Dynamic Drive, at http://www.dynamicdrive.com
//** Created: Jan 7th, 08'. Last updated: June 7th, 2010 to v1.9

//Version 1.9: June 7th, 2010':
//**1) Ajax content support added, so a given header's content can be dynamically fetched from an external file and on demand.
//**2) Optimized script performance by caching header and content container references

tinyMCE.init({
		// General options
 mode : "exact",
		elements : "commentTextArea",
		skin : "cirkuit",
		theme : "cssbro",
		 forced_root_block : "", 
    force_br_newlines : true,
    force_p_newlines : false,
file_browser_callback : 'myFileBrowser',
		plugins : "embed,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,advlist,autosave",
		// Theme options
theme_cssbro_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,link,unlink,forecolor,table",
theme_cssbro_buttons2 : "image,embed,pagebreak,|,fullscreen,code,help",
theme_cssbro_buttons3 : "",
 theme_cssbro_toolbar_location : "top",
		theme_cssbro_toolbar_align : "left",
		theme_cssbro_statusbar_location : "bottom",
		theme_cssbro_resizing : false,
		autosave_ask_before_unload: false,
extended_valid_elements : "iframe[src|width|height|name|align]",
		// Example content CSS (should be your site CSS)
	content_css : "css/content.css",
// Drop lists for link/image/media/template dialogs
		template_external_list_url : "lists/template_list.js",
		external_link_list_url : "lists/link_list.js",
		external_image_list_url : "lists/image_list.js",
		media_external_list_url : "lists/media_list.js",
	relative_urls : true, // Default value
        document_base_url : 'http://localhost/wahana/temp1/',
		// Replace values for the template plugin
		template_replace_values : {
			username : "Some User",
			staffid : "991234"
		},
	  width : "100%",
        height : "300"	
	});
	tinyMCE.init({
		// General options
 mode : "exact",
		elements : "commentTextArea1a",
		skin : "cirkuit",
		theme : "cssbro",
		 forced_root_block : "", 
    force_br_newlines : true,
    force_p_newlines : false,
file_browser_callback : 'myFileBrowser',
		plugins : "embed,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,advlist,autosave",
		// Theme options
theme_cssbro_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,link,unlink,forecolor,table",
theme_cssbro_buttons2 : "image,embed,pagebreak,|,fullscreen,code,help",
theme_cssbro_buttons3 : "",
 theme_cssbro_toolbar_location : "top",
		theme_cssbro_toolbar_align : "left",
		theme_cssbro_statusbar_location : "bottom",
		theme_cssbro_resizing : false,
		autosave_ask_before_unload: false,
extended_valid_elements : "iframe[src|width|height|name|align]",
		// Example content CSS (should be your site CSS)
	content_css : "css/content.css",
// Drop lists for link/image/media/template dialogs
		template_external_list_url : "lists/template_list.js",
		external_link_list_url : "lists/link_list.js",
		external_image_list_url : "lists/image_list.js",
		media_external_list_url : "lists/media_list.js",
	relative_urls : true, // Default value
        document_base_url : 'http://localhost/wahana/temp1/',
		// Replace values for the template plugin
		template_replace_values : {
			username : "Some User",
			staffid : "991234"
		},
	  width : "100%",
        height : "100"	
	});
tinyMCE.init({
		// General options
 mode : "exact",
		elements : "commentTextArea2a",
		skin : "cirkuit",
		theme : "cssbro",
		 forced_root_block : "", 
    force_br_newlines : true,
    force_p_newlines : false,
file_browser_callback : 'myFileBrowser',
		plugins : "embed,pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,advlist,autosave",
		// Theme options
theme_cssbro_buttons1 : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,formatselect,link,unlink,forecolor,table",
theme_cssbro_buttons2 : "image,embed,pagebreak,|,fullscreen,code,help",
theme_cssbro_buttons3 : "",
 theme_cssbro_toolbar_location : "top",
		theme_cssbro_toolbar_align : "left",
		theme_cssbro_statusbar_location : "bottom",
		theme_cssbro_resizing : false,
		autosave_ask_before_unload: false,
extended_valid_elements : "iframe[src|width|height|name|align]",
		// Example content CSS (should be your site CSS)
	content_css : "css/content.css",
// Drop lists for link/image/media/template dialogs
		template_external_list_url : "lists/template_list.js",
		external_link_list_url : "lists/link_list.js",
		external_image_list_url : "lists/image_list.js",
		media_external_list_url : "lists/media_list.js",
	relative_urls : true, // Default value
        document_base_url : 'http://localhost/wahana/temp1/',
		// Replace values for the template plugin
		template_replace_values : {
			username : "Some User",
			staffid : "991234"
		},
	  width : "100%",
        height : "300"	
	});
