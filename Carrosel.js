document.addEventListener("DOMContentLoaded", function () {
  const botoes = document.querySelectorAll(".depoimento .seta");
  const conteudos = document.querySelectorAll(".depoimento .conteudo");

  let atual = 0;
  let intervalo;

  function mostrar(index) {
    conteudos.forEach((el, i) => {
      el.classList.toggle("ativo", i === index);
    });
  }

  botoes[0].addEventListener("click", () => {
    atual = (atual - 1 + conteudos.length) % conteudos.length;
    mostrar(atual);
  });

  botoes[1].addEventListener("click", () => {
    atual = (atual + 1) % conteudos.length;
    mostrar(atual);
  });

  function iniciarAutoPlay() {
    intervalo = setInterval(() => {
      atual = (atual + 1) % conteudos.length;
      mostrar(atual);
    }, 5000);
  }

  document.querySelector(".depoimento").addEventListener("mouseenter", () => {
    clearInterval(intervalo);
  });

  document.querySelector(".depoimento").addEventListener("mouseleave", () => {
    iniciarAutoPlay();
  });

  mostrar(atual);
  iniciarAutoPlay();
});
