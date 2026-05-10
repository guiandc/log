def main():
    #EM SEGUIDA ADICIONE LOGS EM CADA UMA DAS FUNÇÕES DO PROJETO
    try:
        print('Hello World')
        func_log.logging.info(f"-------SUCCESSFUL PRINTING!") #<=== MENSAGEM DE SUCESSO
    except:
        func_log.logging.error("===> ERROR: DURING MESSAGE PRINTING. :( ") #<=== MENSAGEM DE ERRO

if __name__ == '__main__':
    import functions_logging as func_log # <== Instancia o logger
    main()
