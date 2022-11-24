# Neste arquivo contem todos os formulario por aplicação

from django import forms # modulo para formulario
from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    assunto = forms.CharField(label='Assunto',max_length=500)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f' Nome: {nome}\n Email: {email}\n Assunto: {assunto}\n Mensagem: {mensagem}\n'
       
        mail = EmailMessage(
            subject='Email enviado pelo sistema django 2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to = ['contato@seudominio.com.br',],
            headers={'Reply-to': email}
        )
        mail.send() # método para enviar email


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
