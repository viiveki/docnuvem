from kivy.app import App
from kivy.core.window import Window

import controller.mail as mailsender
import model.plano as plano
import model.email as email
import model.cliente as cliente

def teste_insere_plano():
    result = plano.new_plano(4, "DOCNUVEM - Teste")
    print(result)

class Docmail(App):
    def build(self):
        Window.size = (800, 600)
        return super().build()

if __name__ == '__main__':
    Docmail().run()

    # teste_insere_plano()
    #mailsender.send_email()
    #print(plano.get_by_id(4))