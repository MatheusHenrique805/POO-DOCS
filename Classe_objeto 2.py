import datetime
class postagem():
    #Prof. Rogério não consegui botar a hora da publicação da postagem com o datetime, mas depois vou ver se consigo aí lhe mostro quarta
    data_publi = None
    horario_publi = None
    legenda = None
    tipo = None
    nome_dono = None
    curtidas = 0
    comentarios = 0
    compartilhamentos = 0
    
    
    
    def curtiu(self):
        self.curtidas += 1
    
    def comentou(self):
        self.comentarios += 1    
        
    def compartilhou(self):
        self.compartilhamentos += 1

post = postagem()
def postar():
    data = datetime.date.today()
    usuario = input('Usuário: ')
    tipo = input('Imagem/Vídeo: ')
    legenda = input('Insira a legenda da postagem: ')
    return usuario, legenda, tipo, data

    
def postagem():
    print('-'*70)
    print(f'{post.data_publi}')
    print(f'{post.nome_dono} postou uma {post.tipo} com a legenda: "{post.legenda}"                                    |')
    print('''
             ___________________
            |                   |
            |                   |
            |                   |
            |                   |
            |                   |
            |                   |
            |                   |
            |___________________|
            
    ''')
    print(f'{post.curtidas} curtidas {post.comentarios} comentários {post.compartilhamentos} compartilhamentos                          |')
    print('-'*70,'\n')


def interagir_post():
    while True:
        try:
            escolha = int(input('1 - curtir\n2 - comentar\n3 - compartilhar\n4 - Ver comentários\n5 - Sair da postagem\n'))
            if escolha < 6: break
        except:
            print('Opção não encontrada. Tente novamente.')
    return escolha

    
def main():
    post.nome_dono,post.legenda,post.tipo, post.data_publi = postar()
    postagem()
    listcoment = {}
    while True:
        escolha = interagir_post()
        if escolha == 1:
            post.curtiu()
            postagem()
        elif escolha == 2:
            nome = input('Nome da conta:')
            texto = input('Digite logo abaixo seu comentário\n')
            listcoment[nome] = f'{texto}' 
            if texto == '':
                pass
            else:
                post.comentou()
                postagem()
                
        elif escolha == 3:
            post.compartilhou()
            postagem()
            
        elif escolha == 4:
            print(f'{listcoment}')
            input('Aperte "Enter" para encerrar a visualização de comentários\n')
        else:
            postagem()
            break
            
if __name__ == '__main__':
    main()