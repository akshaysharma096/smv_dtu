var forum = (function(){

	function add_question(){
		console.log("popopopopop")

		var name = email.value
		var question  = text.value
		console.log(question)
		if (question.length <=1 ) {
			$('#error').html('please enter the query before clicking submit')
				return;
		}
		$.ajax({
			url:'add/',
			method:'GET',
			data:{
				'name':name,
				'text':question
			},
			success:function(content){
			$("#question").html(" ")
			$('#text').val("");
			$('#email').val("");
				$('#error').html('')
				$.ajax({
					url:'content/',
					method:'GET',
					// data:{

					// },
					success:function(content){
					console.log("qweeqweqwweqw")
					var temp = content.ques;
					var num=0;
					console.log(content.heading.length)
						for(var i =0 ;i<content.heading.length;i++){

						$("#question").append("<div class= 'doubt_div_ques' ><p class='back_content'>" + content.question[i] + "</p>" + "-" + content.heading[i]+"</div>")
						$("#question").append("<div class = 'ans_div_back'><textarea rows ='10' cols = '70' name = 'ans_description' class = 'ans_text' placeholder= 'enter your query...'' ></textarea><br/><button type='button' class =' btn btn-outline-primary ans_submit'>Submit</button></div> <div id = '"+ content.ques_id[i]+ "' class =  'show_ans'></div><button class = 'more_solution'>more answers...</button>")	

						}
						// var temp;
						var temp = content.temp ;
						console.log(content.sol_save.length)
						for(var i =0;i<content.sol_save.length;i++){
							var id = "#" + content.sol_save_id[i]
									$(id).append("<div><p class='back_content'>" + content.sol_save[i] + "</p></div>")

							// 	if(num < 2 ){
							// 		console.log(content.sol_save[i])
							// 		$(id).append("<div><p class='back_content'>" + content.sol_save[i] + "</p></div>")
							// 		num = num + 1 ;
							// 	}

							// }
							// else{
							// 		num = 0;
							// 		temp = content.sol_save_id[i]
							// 		i=i-1;
							// }
						}

						// for(var i = 0;i<content.sol_save.length;i++){
							
						// 		if(i ==0){
						// 			var id = content.sol_save[i]
						// 					$(id).append("<div><p class='back_content'>" + content.sol_save[i] + "</p></div>")
						// 			temp = content.sol_save_id[i]
						// 		}
						// 		else{
						// 			if(temp == content.sol_save_id[i]){
						// 				var id = content.sol_save_id[i]

						// 				if(num < 2){
						// 				$(id).append("<div><p class='back_content'>" + content.sol_save[i] + "</p></div>")
						// 				num++;
						// 				}
						// 			}
						// 			else{
									
						// 				temp = content.sol_save_id[i];
						// 				num = 0;
						// 				continue;
						// 			}

						// 		}
						// 	}
						


					},error:function(){

					}
				})
			},
			error:function(){
				console.log("problem_1");

			}

		})
	}
	$(document).on('ajaxComplete',function(){
		$(".ans_submit").off('click').click(function(){
		var ques = $(this).parent().prev().find("p").text()
		console.log("question is:")
		console.log(ques)
		var sol = $(this).siblings()[0].value
		$.ajax({
			url:'addans/',
			method:'GET',
			data:{
				'question':ques,
				'solution':sol
			},
			success:function(content){
			console.log("qweeqweqwweqwSTEP1")

			var id = "#" + content.ques_id
			$(id).html("")
			$(id).append("<div><p class='back_content'>" + content.ansit + "</p></div>")

			// $("#question").html(" ")
			// $('#text').val("");
			// $('#email').val("");
			// 	$('#error').html('')
				// $.ajax({
				// 	url:'upload/',
				// 	method:'GET',
				// 	// data:{

				// 	// },
				// 	success:function(content){
				// 	console.log("qweeqweqwweqw")

				// 		// for(var i =0 ;i<content.heading.length;i++){
				// 		// 	$("#question").append("<div><p>" + content.answer[i] + "</p>" + "-" + content.heading[i]+ "</div>")
				// 		// $("#question").append("	<input type = 'ans_text' name = 'first_name' id ='email'/><br/><textarea rows ='10' cols = '70' name = 'ans_description' id = 'text' placeholder= 'enter your query...'' ></textarea><br/><button id ='ans_submit'>Submit</button>")	

				// 		// }


				// 	},error:function(){

				// 	}
				// })
			},
			error:function(){
				console.log("problem_2");

			}

		})
		})
	})
	$(document).on('ajaxComplete',function(){
	$(".more_solution").off('click').click(function(){
	var pressed_ques_id = $(this).prev().attr("id").split('#')[0];
	console.log(pressed_ques_id)
	$.ajax({
		url:'all_ans/',
		method:'GET',
		data:{
			'ques_id':pressed_ques_id,
		},
		success:function(context){
			var id ="#" + pressed_ques_id
			$(id).html("")
			for(var i = context.ans.length-1;i>=0;i--){
				
				$(id).append("<div><p class='back_content'>" + context.ans[i] + "</p></div>")

			}
			console.log(context.ans)
			console.log("all_answer_shown")

		},error:function(){
			console.log("ans_not_shown")
		}

	})
	})
})

	$(".ans_submit_1").click(function(){
		var ques = $(this).parent().prev().find("p").text()
		var sol = $(this).siblings()[0].value
		console.log(sol)
		console.log(ques)
		$.ajax({
			url:'addans/',
			method:'GET',
			data:{
				'question':ques,
				'solution':sol
			},
			success:function(content){
			console.log("qweeqweqwweqwSTEP1")

			var id = "#" + content.ques_id
			$(id).html("")
			$(id).append("<div><p class='back_content'>" + content.ansit + "</p></div>")

			// $("#question").html(" ")
			// $('#text').val("");
			// $('#email').val("");
			// 	$('#error').html('')
				// $.ajax({
				// 	url:'upload/',
				// 	method:'GET',
				// 	// data:{

				// 	// },
				// 	success:function(content){
				// 	console.log("qweeqweqwweqw")

				// 		// for(var i =0 ;i<content.heading.length;i++){
				// 		// 	$("#question").append("<div><p>" + content.answer[i] + "</p>" + "-" + content.heading[i]+ "</div>")
				// 		// $("#question").append("	<input type = 'ans_text' name = 'first_name' id ='email'/><br/><textarea rows ='10' cols = '70' name = 'ans_description' id = 'text' placeholder= 'enter your query...'' ></textarea><br/><button id ='ans_submit'>Submit</button>")	

				// 		// }


				// 	},error:function(){

				// 	}
				// })
			},
			error:function(){
				console.log("problem_2");

			}

		})
		})


	$(".more_solution_1").off('click').click(function(){
	var pressed_ques_id = $(this).prev().attr("id").split('#')[0];
	console.log(pressed_ques_id)
	$.ajax({
		url:'all_ans/',
		method:'GET',
		data:{
			'ques_id':pressed_ques_id,
		},
		success:function(context){
			var id ="#" + pressed_ques_id
			$(id).html("")
			for(var i = context.ans.length-1;i>=0;i--){
				
				$(id).append("<div><p class='back_content'>" + context.ans[i] + "</p></div>")

			}
			console.log(context.ans)
			console.log("all_answer_shown")

		},error:function(){
			console.log("ans_not_shown")
		}

	})
	})

	function init(config){
		submit_click =document.getElementById(config['submit'])
		email =document.getElementById(config['email'])
		text =document.getElementById(config['text'])
		box = document.getElementById(config['box'])
		ans_submit = document.getElementById(config['ans_submit'])
		// ans_submit.addEventListener('click',add_answer)
		submit_click.addEventListener('click',add_question) 
	

	}
	
	return{
		init:init
	}

}());



