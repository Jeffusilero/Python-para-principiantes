let noButtonClickCount = 0; // Contador para el botón "No"
let noButtonState = 0; // Estado actual del botón "No"

// Mostrar el gif inicial
document.getElementById('gifContainer').style.display = 'block';

document.getElementById('siBtn').addEventListener('click', function() {
    // Ocultar el gif triste y mostrar el gif feliz
    document.getElementById('sadGifContainer').style.display = 'none';
    document.getElementById('sadGifContainer1').style.display = 'none';
    document.getElementById('sadGifContainer2').style.display = 'none';
    document.getElementById('sadGifContainer3').style.display = 'none';
    document.getElementById('sadGifContainer4').style.display = 'none';
    document.getElementById('sadGifContainer6').style.display = 'none';
    document.getElementById('happyGifContainer').style.display = 'none';
    document.getElementById('happyGifContainer2').style.display = 'none';
    document.getElementById('happyGifContainer3').style.display = 'none';
    document.getElementById('happyGifContainer4').style.display = 'none';
    document.getElementById('gifContainer').style.display = 'none';
    document.getElementById('sadGifContainer5').style.display = 'block';

    // Ocultar los botones "Pregunta Sí" y "No "
    document.getElementById('question').style.display = 'none';
    document.getElementById('siBtn').style.display = 'none';
    document.body.classList.add('bg-green');
    document.getElementById('noBtn').style.display = 'none';

    // Mostrar el mensaje específico
    document.getElementById('messageContainer').style.display = 'block';
    document.getElementById('messageContainer').innerHTML = "Feliz San Valentin Mi Amor";



});


document.getElementById('noBtn').addEventListener('click', function() {
    switch (noButtonState) {
        case 0:
            // Primera vez haciendo clic en "No"
            document.getElementById('happyGifContainer').style.display = 'none';
            document.getElementById('gifContainer').style.display = 'none';
            document.getElementById('happyGifContainer4').style.display = 'none';
            document.getElementById('sadGifContainer').style.display = 'block';

            // Modificar el botón "No"
            document.getElementById('noBtn').innerHTML = 'Te prometo que sera inolvidable';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
    
            
            document.getElementById('siBtn').style.fontSize = '40px';
            document.getElementById('siBtn').style.padding = '10px 20px';

            
            noButtonClickCount++;
            noButtonState++;
            break;

        case 1:
            // Segunda vez haciendo clic en "No"

            document.getElementById('noBtn').innerHTML = '¿Realmente estas seguro?';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('sadGifContainer').style.display = 'none';
            document.getElementById('sadGifContainer2').style.display = 'block';

            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '45px';
            document.getElementById('siBtn').style.padding = '20px 30px';
        
            noButtonState++;
            break;

        case 2:
    
            document.getElementById('noBtn').innerHTML = 'Piensalo de nuevo';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('sadGifContainer').style.display = 'none';
            document.getElementById('sadGifContainer2').style.display = 'none';
            document.getElementById('sadGifContainer1').style.display = 'block';

            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '30px 40px';
        
            noButtonState++;
            break;
        
        case 3:
            document.getElementById('noBtn').innerHTML = 'Estás seguro de verdad, ¿eh?';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('sadGifContainer').style.display = 'none';
            document.getElementById('sadGifContainer2').style.display = 'none';
            document.getElementById('sadGifContainer1').style.display = 'none';
            document.getElementById('sadGifContainer4').style.display = 'block';
    

            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '40px 50px';
        
            noButtonState++;
            break;
        case 4:
            document.getElementById('noBtn').innerHTML = 'Vamos atrevete a decir que si';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('sadGifContainer').style.display = 'none';
            document.getElementById('sadGifContainer4').style.display = 'none';
            document.getElementById('happyGifContainer3').style.display = 'none';
            document.getElementById('sadGifContainer3').style.display = 'block';
        


            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '50px 60px';
    
            noButtonState++;
            break;
        case 5:
            document.getElementById('noBtn').innerHTML = 'Solo piensa en ello';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('happyGifContainer3').style.display = 'block';
            document.getElementById('sadGifContainer3').style.display = 'none';

            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '60px 70px';

            noButtonState++;
            break;
        case 6:
            document.getElementById('noBtn').innerHTML = 'Seria perfecto que lo reconsideres';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('happyGifContainer2').style.display = 'block';
            document.getElementById('happyGifContainer3').style.display = 'none';


            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '70px 80px';
            
            noButtonState++;
            break;
        case 7:
            document.getElementById('noBtn').innerHTML = 'Estaré muy triste';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('happyGifContainer').style.display = 'block';
            document.getElementById('happyGifContainer2').style.display = 'none';

            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '80px 90px';

            noButtonState++;
            break;
        case 8:
            document.getElementById('noBtn').innerHTML = 'No dejes que el miedo te detenga';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('sadGifContainer6').style.display = 'block';
            document.getElementById('happyGifContainer').style.display = 'none';
            

            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '90px 100px';
    
            noButtonState++;
            break;

        case 9:
            document.getElementById('noBtn').innerHTML = 'Por Favor';
            document.getElementById('noBtn').style.backgroundColor = '#F1330A';
            document.getElementById('happyGifContainer4').style.display = 'block';
            document.getElementById('sadGifContainer6').style.display = 'none';
        
            
            // Hacer que el botón "Sí" crezca
            document.getElementById('siBtn').style.fontSize = '50px';
            document.getElementById('siBtn').style.padding = '100px 110px';
        
            noButtonState = 0;
            break;
        

        default:
            // Por si acaso, maneja cualquier otro caso aquí
            break;
    }
});


