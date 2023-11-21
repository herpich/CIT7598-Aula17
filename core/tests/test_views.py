"""from django.test import TestCase
from django.test import Client #permite enviar solicitações HTTP simuladas
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.dados = {
            'nome': 'Fabrício Herpich',
            'email': 'fabricio.herpich@gmail.com',
            'assunto': 'Meu assunto',
            'mensagem': 'Minha mensagem',
        }

        self.cliente = Client() #agora com o cliente é possível executar post/get/

    def test_form_valid(self):
        request = self.cliente.post(reverse_lazy('index'), data=self.dados)
        self.assertEquals(request.status_code, 302) # 302 - Redirecionamento

    def test_form_invalid(self):
        dados2 = {
            'nome': 'Fabrício Herpich',
            'assunto': 'Meu assunto',
        }
        request = self.cliente.post(reverse_lazy('index'), data=dados2)
        self.assertEquals(request.status_code, 200) # 200 - Ok

"""