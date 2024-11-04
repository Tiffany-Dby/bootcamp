from ninja import Router, ModelSchema, Schema
from polls.models import Question, Choice

router = Router()

class ChoiceSchema(ModelSchema):
  class Meta:
    model = Choice
    fields = ["id", "choice_text", "votes"]

class QuestionSchema(ModelSchema):
  class Meta:
    model = Question
    fields = ["id", "question_text", "pub_date"]

  choices: list[ChoiceSchema]

class AddQuestionSchema(Schema):
  question_text: str
  choices: list[str]

@router.post("/create_question", response=QuestionSchema)
def add(request, add_question: AddQuestionSchema):
  question = Question.objects.create(
    question_text=add_question.question_text, 
  )

  for choice in add_question.choices:
    Choice.objects.create(
      choice_text=choice, 
      question=question,
    )

  return question

@router.get("/question/{question_id}", response=QuestionSchema)
def get(request, question_id: int):
  return Question.objects.get(pk=question_id)