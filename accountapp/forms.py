#폼을 상속받아 커스터마이징
from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        self.fields['username'].disabled = True # username칸 비활성화
