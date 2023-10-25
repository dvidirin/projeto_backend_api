## Guia para atualizar o Fork com a Branch Principal

* ### Siga as etapas abaixo:

1. **Verifique se seu controle remoto já tem o "upstream"**
```
git remote -v
```
2. **Caso não tenha, adicione o repositório original como um controle remoto chamado "upstream"**
```
git remote add upstream https://github.com/dvidirin/projeto_backend.git
```
3. **Verifique se o controle remoto "upstream" foi adicionado corretamente**
```
git remote -v
```
4. **Buscar as alterações do repositório original (upstream)**
```
git fetch upstream
```
5. **Mesclá-las com o seu branch local principal**
```
git merge upstream/main
```
6. **Envie as alterações para o seu fork no GitHub**
```
git push origin main
```
