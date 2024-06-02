const new_file_button = document.getElementById('new-file-button')

//new file set form
const new_file_close_button = document.getElementById('new-file-modal-close-x')
const new_file_modal = document.getElementById('new-file-modal')
const new_file_modal_form = document.getElementById('new-file-modal-form')


function getCookie(name) {

	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}


function sendFormfile(form) {
	var form_file = new FormData(form)

	let requestOptions = {

		method: 'POST',
		headers: {
			"X-CSRFToken": getCookie('csrftoken'),
		},
		body: form_file
	}

	fetch('./', requestOptions)

		.then(response => {
			if (response.ok) {
				return response.json();
			}
			throw new Error('Network response was not ok.');
		})

		.then(file => {
			console.log(file)
		})

		.catch(error => {
			console.error('There was a problem with the fetch operation:', error);
		})
}


function openModal(modal) {
	modal.style.display = 'block'
}


function closeModal(modal) {
	modal.style.display = 'none'
}

// open modal
new_file_button.addEventListener('click', function(e) {
	openModal(new_file_modal)
})

// send the file to the server
new_file_modal_form.addEventListener('submit', function(e) {
	e.preventDefault()
	
	$('#my-file').click();

	//sendFormfile(new_file_modal_form)

	//new_file_modal_form.reset()

	//closeModal(new_file_modal)
})

// close new file set modal
new_file_close_button.addEventListener('click', function(e){
	closeModal(new_file_modal)
})
