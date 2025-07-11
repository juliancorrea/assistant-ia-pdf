#!/bin/bash

# Script para executar o Assistente IA PDF no macOS ARM64

echo "🚀 Iniciando o Assistente Inteligente..."
echo ""

# Verificar se está no diretório correto
if [ ! -f "app.py" ]; then
    echo "❌ Erro: Execute este script no diretório do projeto"
    exit 1
fi

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual ARM64..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se as dependências estão instaladas
if [ ! -f "venv/lib/python3.12/site-packages/streamlit/__init__.py" ]; then
    echo "📥 Instalando dependências..."
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
    echo "✅ Dependências instaladas"
fi

# Executar o aplicativo
echo "🎯 Executando o Assistente IA PDF..."
echo "📱 Acesse: http://localhost:8501"
echo ""

streamlit run app.py