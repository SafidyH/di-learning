const form = document.getElementById('libform');
const libButton = document.getElementById('lib-button');
const storyElement = document.getElementById('story');

form.addEventListener('submit', function(event) {
  event.preventDefault();

  const noun = document.getElementById('noun').value;
  const adjective = document.getElementById('adjective').value;
  const person = document.getElementById('person').value;
  const verb = document.getElementById('verb').value;
  const place = document.getElementById('place').value;

  if (!noun || !adjective || !person || !verb || !place) {
    console.error('Please fill in all the fields.');
    return;
  }

  const story = `Once upon a time, there was a ${adjective} ${noun} named ${person}. They loved to ${verb} in ${place}. The end.`;
  storyElement.textContent = story;
});

libButton.addEventListener('click', function() {
  const stories = [
    'The quick brown fox jumps over the lazy dog.',
    'She sells seashells by the seashore.',
    'How much wood would a woodchuck chuck if a woodchuck could chuck wood?'
  ];

  const randomIndex = Math.floor(Math.random() * stories.length);
  storyElement.textContent = stories[randomIndex];
});