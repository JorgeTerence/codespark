const usernames = [
	'Sr_André',
	'Fernanda',
	'Mark_Zuckerberg',
	'Linus_Torvalds',
	'Richard_Stallman',
	'Bruno',
	'Queijo_prato',
	'EuOdeioJava',
	'naki',
	'batata',
	'Peter_Parker',
	'Skynet',
	'Goku',
	'Pikachu',
	'Optimus Prime',
];

const usernameField = document.getElementsByName('username')[0];

usernameField.placeholder = usernames[Math.round(Math.random() * 14)];