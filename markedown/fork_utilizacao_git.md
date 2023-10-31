## Guia para dar Fork e fazer suas alterações

* ### Siga as etapas abaixo:

1. **Verifique sua configuração de usuário global no git.**
```
git config --list
```
2. **Se a configuração do user.name ou user.email estiver incorreto.**
```
git config --global user.name 'FirstName LastName'
```
```
git config --global user.email 'your_email@domain.com.br'
```
3. **Faça um fork deste repositório: [https://github.com/dvidirin/projeto_backend.git](https://github.com/dvidirin/projeto_backend.git).**

4. **Faça o clone deste repositório.**
```
git clone https://github.com/SEU_USUARIO/projeto_backend.git .
```
5. **LEMBRE-SE: Antes de Alterar e Antes de Commitar, atualize seu repositório para evitar conflito.**
```
git pull
```
6. **LEMBRE-SE: idem 5 e siga o [Guia para atualizar o Fork com a Branch Principal](atualizar_fork_git.md).**
7. **Antes de Commitar, Adicionar no Stage.**
- Para adicionar tudo.
```
git add .
```
```
git add *
```
- Para adicionar um arquivo expecifico.
```
git add nome_arquivo.ext
```
- Para adicionar mais arquivos expecifico.
```
git add nome_arquivo.ext outro_nome_arquivo.ext
```
8. **Para saber o status do repositório.**
```
git status
```
9. **Para commitar, coloque uma mensagem, caso necessário adicione uma descrição mais detalhada.**
```
git commit -m "Minha contribuição" -m "Minha descrição"
```
10. **Não esquece que depois do commit, precisa enviar para o GitHup**
```
git push
```
11. **Para ver o relatório dos commites**
```
git log
```

### OBSERVAÇÃO SOBRE CONFLITO

**Caso de conflito, por esquecer de atualizar o repoitório local.**
```
git pull
```

**Caso de conflito por alterar algo no mesmo lugar.**
```
git pull
```
**Que o VS Code vai deixar escolher as opções para resolver, depois é só commitar.**
```
git commit -m "Resolvi conflito de _ " -m "Minha descrição"
```

### Mostrar as alterações que foram feitas para o Grupo antes de fazer o Pull Request

- Mostrando seu link no GitHub com o Fork

* Após aprovado, siga o [Guia para fazer Pull Request](pull_request_git.md)
  
---
* **Caso queira ter uma experiência melhor com o Git, adicione a extensão: `GitLens`**
---

