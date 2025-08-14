// Elementos principais
const form = document.getElementById('newsForm');
const titleInput = document.getElementById('newsTitle');
const contentInput = document.getElementById('newsContent');
const submitBtn = document.querySelector('.submit-btn');
const resultsSection = document.getElementById('resultsSection');
const resultsList = document.getElementById('resultsList');


// Envio do formulário
//form.addEventListener('submit', function (e) {  
//    e.preventDefault();
//
//    const title = titleInput.value || 'Notícia sem título';
//    const content = contentInput.value.trim();
//
//    // Validação mínima
//    if (content.length < 50) {
//        alert('Por favor, cole um texto mais longo para análise.');
//        contentInput.focus();
//        return;
//    }
//
//    // Aqui chama a análise da IA
//    // mostrando o resultado simulado
//    const status = 'Verdadeira'; // placeholder simples
//    addResult(title, content, status);
//
//    // Mostrar seção de resultados
//    resultsSection.style.display = 'block';
//    resultsSection.scrollIntoView({ behavior: 'smooth' });
//
//    // Limpar campo de conteúdo
//    contentInput.value = '';
//});

// Adicionar resultado na tela
function addResult(title, content, status) {
    const info = {
        'Verdadeira': { text: 'VERDADEIRA ✅', advice: '✅ Compartilhe com segurança.' },
        'Falsa': { text: 'FALSA ❌', advice: '🚫 NÃO compartilhe.' },
        //'Partial': { text: 'PARCIAL ⚠️', advice: '⚠️ Tenha cuidado ao compartilhar.' }
    };

    const preview = content.length > 200 ? content.substring(0, 200) + '...' : content;

    const resultItem = document.createElement('div');
    resultItem.className = 'result-item';
    resultItem.innerHTML = `
        <div class="result-header">
            <div class="result-title">${title}</div>
            <span class="status-badge status-${status}">${info[status].text}</span>
        </div>
        <div class="result-content">"${preview}"</div>
        <div class="result-explanation">
            <p><strong>${info[status].advice}</strong></p>
        </div>
    `;
    resultsList.insertBefore(resultItem, resultsList.firstChild);
}

// Limpar resultados
function clearResults() {
    if (confirm('Tem certeza que deseja limpar todos os resultados?')) {
        resultsList.innerHTML = '';
        resultsSection.style.display = 'none';
        titleInput.value = '';
        contentInput.value = '';
        contentInput.focus();
    }
}


// Foco automático no campo de conteúdo
addEventListener('load', () => contentInput.focus());
