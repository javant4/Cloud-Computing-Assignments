$(function(){
	$('button').click(function(){
		var date = $('#dateWeather').val();
		$.ajax({
			url: '/weather',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
