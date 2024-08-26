var email = "";
function handleLogin() {
    // Obtém o valor do campo de texto do nome de usuário
    email = document.getElementById('email').value;
    
    // Exibe o nome de usuário no console (ou você pode fazer outra coisa com ele)
    console.log('Usuário digitado:', email);
    
    // Aqui você pode adicionar mais lógica, como enviar os dados para um servidor

   if(email === "usuario"){
    redirectToPage();
    }else if(email === "ADM"){
    redirectToPage();
    }
    else{
    window.alert("usuario nao encontrado")
    } 
 

    gravaUsu();
    return email;
}


function redirectToPage() {
    var email = document.getElementById('email').value;
            
    // Armazena o nome de usuário no sessionStorage
    
    window.location.href = 'treinamentos.html';
    console.log('Usuário digitado:', email);
    window.alert(email)
   return email;
}

var aux = gravaUsu();
function gravaUsu(){
    email = document.getElementById('email').value;

    console.log('teste gravausu ' + email);
    return email;
}


function validaUsu(){
   var email = gravaUsu();
    window.alert(email);
    console.log('A página foi carregada e a função foi chamada.');
if (email === "usuario") {
    document.getElementById('var_usu').textContent = `${email}`;
    sessionStorage.removeItem('var_usu');

}else if (email === "ADM"){
    document.getElementById('var_usu').textContent = `${email}`;
    sessionStorage.removeItem('var_usu');
}
}

