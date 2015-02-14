// add active class menu


$(document).ready(function(){
	add_active_class()
	
})

function add_active_class(){
	var slug = window.location.href
	var host = window.location.host
	var protocol = window.location.protocol
	slug = slug.split(protocol+'//'+host)
	slug = slug[1]
	el = $('a[href="'+slug+'"]')
	el.parent().addClass('active')
	el.parent().parent().parent('li').addClass('active')	
}