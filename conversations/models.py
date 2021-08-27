from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    participants = models.ManyToManyField(
        "users.User", related_name="conversation", blank=True
    )

    def __str__(self):
        usernames = []  # 강의8.2 - 2. 음.. 어렵다..집중력 떨어지네..여기선.
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)  # 흠.join메소드.. 신기. 대화방에 있는 사람들 목록 보여주는 느낌.

    def count_messages(self):  # 강의8.2 - 3. 메세지 수 표시하기.
        return self.messages.count()
        # conversation은 self.messages값을 갖는다 @@@@@@@
        # 왜냐하면 message가 conversation값을 갖고있는데.foreign key로.
        # 근데 related_name을 써줬으니까 역참조 가능. @@@@@@*******

    count_messages.short_description = "number of messages"  # 제목 바꿔주기.

    def count_participants(self):
        return self.participants.count()

    count_messages.short_description = "number of participants"  # 제목 바꿔주기.


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says: {self.message}"
