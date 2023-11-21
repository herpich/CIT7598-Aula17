import uuid
from django.test import TestCase
from model_mommy import mommy
from core.models import get_file_path

class GetFilePathTestCase(TestCase):
    def setUp(self):
        # vamos criar um arquivo para conseguirmos comparar
        # seguindo a mesma estrutura da função lá do Model (algum_uuid.png)
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))
        # testando se estrutura do setUp é igual a submetida para a função get_file_path
        # criamos um arquivo seguindo o padrão (em setUp) e criamos outro arquivo usando
        # a própria função (que veio lá do Model, em test_get_file_path).

class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')
        # mommy vai nos ajudar a gerar um serviço

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)

class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)

class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)