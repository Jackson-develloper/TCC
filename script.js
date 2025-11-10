// Aplicar mascara cpf
function mascaracpf(input){
    // remove os caracteres que nao sao numeros
    let valor = input.value.replace(/\D/g, '');
    // aciona ponto após 3 digitos
    valor = valor.replace(/(\d{3})(\d)/, '$1.$2')
    // aciona ponto após 6 digitos
    valor = valor.replace(/(\d{3})(\d)/, '$1.$2')
 
    valor = valor.replace(/(\d{3})(\d{1,2})$/, '$1-$2')
   
    input.value = valor;
}
// mascara telefone
function mascaratelefone(input){
    // remove os caracteres que nao sao numeros
    let valor = input.value.replace(/\D/g, '');
    // aciona ponto após 3 digitos
    valor = valor.replace(/(\d{2})(\d)/, '($1) $2')
    // aciona ponto após 6 digitos
    valor = valor.replace(/(\d{5})(\d)/, '$1-$2')
 
 
 
    input.value = valor;
}
 
function mascaraCEP(input){
      let valor = input.value.replace(/\D/g, '');
      //Adiciona um traça apos os 5 primeiros digitos
      valor = valor.replace(/(\d{5})(\d)/,'$1-$2')
 
      valor = valor.replace(/(\d{2})(\d)/, '$1.$2')
 
      input.value = valor;
}
 
// aplica a função ao carregar a página
window.onload = function(){
    // aplica a mascara cpf no input com id cpf
    document.getElementById('cpf').addEventListener('input', function(){mascaracpf(this);});
    document.getElementById('telefone').addEventListener('input', function(){mascaratelefone(this);});
   
}
