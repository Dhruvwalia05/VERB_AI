from django.shortcuts import render
import subprocess

def get_moral_and_rating(story):
    query = f"Here's a story: {story}\nNow just tell me the moral of this story and rate it out of 10 (how much it is recommended for children)? (Moral of the Story: & Rating: )"

    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama2', query],
            capture_output=True,
            text=True,
            check=True
        )
        response = result.stdout.strip()
        return response
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def analyze_story(request):
    if request.method == 'POST':
        story = request.POST.get('story', '').strip()  # Get the input story and trim whitespace
        # Assume `get_moral_and_rating` is a function that processes the story and returns a response
        response = get_moral_and_rating(story)
        
        if response:
            # Splitting response into moral and rating parts
            moral, rating = response.split('Rating:')  # Split at 'Rating:' to separate moral and rating
            moral = moral.replace('Moral of the Story: ', '').strip()  # Remove the "Moral of the Story:" prefix
            return render(request, 'chatbot/analyze_story.html', {'moral': moral, 'rating': rating.strip()})
    
    return render(request, 'chatbot/analyze_story.html')

