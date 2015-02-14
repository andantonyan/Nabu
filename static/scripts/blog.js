// alert(article_update)

$(document).on('click', '.more_articles button', function(){
	update_articles();
});


$(document).on('click', '.more_comments button', function(){
	var el = $(this);
	update_comments(el);
});


$(document).on('click', '.remove_article', function(){
	var el = $(this);
	remove_article(el);
});


$(document).on('click', '.remove_comment', function(){
	var el = $(this);
	remove_comment(el);
});



function update_articles(){
	var articles_count = $('.article').length
	// alert(typeof(articles_count))

	jQuery.ajax({
	  url: article_update_url,
	  type: 'POST',
	  dataType: 'html',
	  data: {articles_count: articles_count},
	  complete: function(xhr, textStatus) {
	    //called when complete
	  },
	  success: function(data, textStatus, xhr) {
	    //called when successful
	    $('#artcile_section').append(data)
	  },
	  error: function(xhr, textStatus, errorThrown) {
	    //called when there is an error
	  }
	});
}


function update_comments(el){
	var article = el.attr('article');
	var comments_count = el.attr('count');
	comments_count = parseInt(comments_count);
	jQuery.ajax({
	  url: comment_update_url,
	  type: 'POST',
	  dataType: 'html',
	  data: {comments_count: comments_count, article: article},
	  complete: function(xhr, textStatus) {
	    //called when complete
	  },
	  success: function(data, textStatus, xhr) {
	    //called when successful
	    el.parent().parent().before(data)
	    var new_count = parseInt($(data).filter('.comment').length)
	    // if (new_count == 0) {
	    // 	// alert()
	    // 	el.addClass('class_name')
	    // }
	    new_count += comments_count
	    el.attr('count', new_count);

	  },
	  error: function(xhr, textStatus, errorThrown) {
	    //called when there is an error
	  }
	});
}



function remove_article(el){
	var article = el.attr('article');

	jQuery.ajax({
	  url: article_remove_url,
	  type: 'POST',
	  dataType: 'json',
	  data: {article: article},
	  complete: function(xhr, textStatus) {
	    //called when complete
	  },
	  success: function(data, textStatus, xhr) {
	    //called when successful

	    if(data == true) {

	    	el.parent().parent().parent().parent().parent().remove();
	    }

	  },
	  error: function(xhr, textStatus, errorThrown) {
	    //called when there is an error
	  }
	});
}

function remove_comment(el){
	var comment = el.attr('comment');

	jQuery.ajax({
	  url: comment_remove_url,
	  type: 'POST',
	  dataType: 'json',
	  data: {comment: comment},
	  complete: function(xhr, textStatus) {
	    //called when complete
	  },
	  success: function(data, textStatus, xhr) {
	    //called when successful

	    if(data == true) {

	    	el.parent().parent().parent().parent().parent().remove();
	    }

	  },
	  error: function(xhr, textStatus, errorThrown) {
	    //called when there is an error
	  }
	});
}