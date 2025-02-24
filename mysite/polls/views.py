from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Vote
from .forms import PollForm, ChoiceForm
import json
from django.utils import timezone



# 📌 Displays the list of polls
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

# 📌 Displays a single poll question
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        """Pass user vote data to the template for pre-selecting the radio button."""
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_vote = Vote.objects.filter(user=self.request.user, question=self.object).first()
            context["user_vote"] = user_vote.choice.id if user_vote else None
        else:
            context["user_vote"] = None
        return context

# 📌 Displays poll results
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# 📌 Handles voting logic
@login_required
@csrf_exempt
def vote(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        choice_id = request.POST.get("choice")

        if not choice_id:
            return JsonResponse({"error": "Missing choice parameter"}, status=400)

        if not choice_id.isdigit():
            return JsonResponse({"error": "Invalid choice selected"}, status=400)

        selected_choice = get_object_or_404(Choice, pk=int(choice_id))

        # Fix: Ensure choice is included in get_or_create()
        vote, created = Vote.objects.get_or_create(
            user=request.user,
            question=question,
            defaults={"choice": selected_choice},
        )

        if not created:
            vote.choice = selected_choice
            vote.save()

        return redirect("polls:results", pk=question_id)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)

# 📌 Allows users to create a poll
@login_required
def create_poll(request):
    if request.method == "POST":
        poll_form = PollForm(request.POST)
        choice_forms = [ChoiceForm(request.POST, prefix=str(i)) for i in range(3)]  # 3 default choices

        if poll_form.is_valid() and all(cf.is_valid() for cf in choice_forms):
            poll = poll_form.save(commit=False)
            poll.save()

            for cf in choice_forms:
                choice = cf.save(commit=False)
                choice.question = poll
                choice.save()

            return redirect("polls:index")

    else:
        poll_form = PollForm()
        choice_forms = [ChoiceForm(prefix=str(i)) for i in range(3)]

    return render(request, "polls/create_poll.html", {"poll_form": poll_form, "choice_forms": choice_forms})


# 📌 Displays the list of polls
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

# 📌 Displays a single poll question
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        """Pass user vote data to the template for pre-selecting the radio button."""
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_vote = Vote.objects.filter(user=self.request.user, question=self.object).first()
            context["user_vote"] = user_vote.choice.id if user_vote else None
        else:
            context["user_vote"] = None
        return context

# 📌 Displays poll results
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# 📌 Handles voting logic
@login_required
@csrf_exempt
def vote(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        choice_id = request.POST.get("choice")

        if not choice_id:
            return JsonResponse({"error": "Missing choice parameter"}, status=400)

        if not choice_id.isdigit():
            return JsonResponse({"error": "Invalid choice selected"}, status=400)

        selected_choice = get_object_or_404(Choice, pk=int(choice_id))

        # Fix: Ensure choice is included in get_or_create()
        vote, created = Vote.objects.get_or_create(
            user=request.user,
            question=question,
            defaults={"choice": selected_choice},
        )

        if not created:
            vote.choice = selected_choice
            vote.save()

        return redirect("polls:results", pk=question_id)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)

# 📌 Allows users to create a poll
@login_required
def create_poll(request):
    if request.method == "POST":
        poll_form = PollForm(request.POST)
        choice_texts = request.POST.getlist('choice_text')  # Get list of choice inputs

        if poll_form.is_valid() and all(choice_text.strip() for choice_text in choice_texts):
            poll = poll_form.save(commit=False)
            poll.pub_date = timezone.now()  # Set pub_date explicitly
            poll.save()

            for choice_text in choice_texts:
                Choice.objects.create(question=poll, choice_text=choice_text)

            return redirect("polls:index")  # Redirect to poll list after submission

    else:
        poll_form = PollForm()

    return render(request, "polls/create_poll.html", {"poll_form": poll_form})

@csrf_exempt
def my_post_view(request):
    """Simple test endpoint for debugging POST requests."""
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

    try:
        data = json.loads(request.body)
        return JsonResponse({"message": "POST request received!", "data": data})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON format"}, status=400)