from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Fabrício'
        self.email = 'fabricio.herpich@gmail.com'
        self.assunto = 'Testes com Django'
        self.mensagem = 'Este é um teste do forms do Django.'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        self.form = ContatoForm(data=self.dados)
        # mesma coisa que ocorre na views, com ContatoForm(request.POST)

    def test_send_mail(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        res1 = form1.send_mail()

        form2 = self.form # esse form está recebendo o form do setUp
        form2.is_valid()
        res2 = form2.send_mail()

        self.assertEquals(res1, res2)

