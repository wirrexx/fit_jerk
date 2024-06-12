// timer.js

var interval;
var remainingTime;
var isPaused = false;
var currentExerciseIndex = 0;
var isBreak = false;
var breakDuration = 10; // 10 seconds break
var exercises = [];
var hasRepeated = false; // Flag to check if the workout has been repeated
// Extract exercise data from HTML
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.exercise-item').forEach(function (item) {
        exercises.push({
            name: item.getAttribute('data-name'),
            duration: parseInt(item.getAttribute('data-duration'))
        });
    });
    var timerDisplay = document.querySelector('#timer');
    var message = document.querySelector('#message');
    var pauseResumeButton = document.getElementById('pause-resume-btn');
    var finishButton = document.getElementById('finish-btn');
    var startButton = document.getElementById('start-btn');
    startButton.addEventListener('click', startWorkout);
    pauseResumeButton.addEventListener('click', togglePauseResume);
    finishButton.addEventListener('click', finishWorkout);
    // Initialize timer display
    if (exercises.length > 0) {
        timerDisplay.textContent = formatTime(exercises[0].duration);
    }
});
function formatTime(seconds) {
    var minutes = parseInt(seconds / 60, 10);
    seconds = parseInt(seconds % 60, 10);
    minutes = minutes < 10 ? "0" + minutes : minutes;
    seconds = seconds < 10 ? "0" + seconds : seconds;
    return minutes + ":" + seconds;
}
function startWorkout() {
    if (exercises.length > 0) {
        hasRepeated = false; // Reset the repeat flag
        currentExerciseIndex = 0; // Reset the exercise index
        var firstExercise = exercises[0];
        updateExerciseDisplay(firstExercise.name);
        startTimer(firstExercise.duration, document.querySelector('#timer'), document.querySelector('#message'), function () {
            document.querySelector('#message').textContent = "Exercise Finished";
        });
        hideStartButton();
    }
}
function startTimer(duration, display, message, callback) {
    var timer = duration;
    remainingTime = timer;
    interval = setInterval(function () {
        if (!isPaused) {
            display.textContent = formatTime(timer);
            if (--timer < 0) {
                clearInterval(interval);
                if (callback) callback();
                if (!isBreak) {
                    if (currentExerciseIndex + 1 < exercises.length) {
                        isBreak = true;
                        message.textContent = "Break Time!";
                        startBreakTimer(breakDuration, display, message, function () {
                            isBreak = false;
                            currentExerciseIndex++;
                            var nextExercise = exercises[currentExerciseIndex];
                            message.textContent = "Next Exercise: " + nextExercise.name;
                            updateExerciseDisplay(nextExercise.name);
                            startTimer(nextExercise.duration, display, message, function () {
                                message.textContent = "Exercise Finished";
                            });
                        });
                    } else {
                        if (!hasRepeated) {
                            hasRepeated = true; // Set the repeat flag
                            currentExerciseIndex = 0; // Reset the exercise index
                            message.textContent = "Repeating Workout!";
                            var firstExercise = exercises[0];
                            updateExerciseDisplay(firstExercise.name);
                            startTimer(firstExercise.duration, display, message, function () {
                                message.textContent = "Exercise Finished";
                            });
                        } else {
                            hidePauseButton();
                            message.textContent = "Workout Finished";
                            document.getElementById('finish-btn').style.display = 'inline';
                        }
                    }
                }
            }
        }
    }, 1000);
}
function startBreakTimer(duration, display, message, callback) {
    var timer = duration;
    remainingTime = timer;
    interval = setInterval(function () {
        if (!isPaused) {
            display.textContent = formatTime(timer);
            if (--timer < 0) {
                clearInterval(interval);
                if (callback) callback();
            }
        }
    }, 1000);
}
function togglePauseResume() {
    var button = document.getElementById('pause-resume-btn');
    if (isPaused) {
        button.textContent = "Pause";
        isPaused = false;
    } else {
        button.textContent = "Resume";
        isPaused = true;
    }
}
function updateExerciseDisplay(exerciseName) {
    var exerciseItems = document.querySelectorAll('.exercise-item');
    exerciseItems.forEach(function (item) {
        if (item.getAttribute('data-name') === exerciseName) {
            item.style.display = 'list-item';
        } else {
            item.style.display = 'none';
        }
    });
}
function hideStartButton() {
    document.getElementById('start-btn').style.display = 'none';
}
function hidePauseButton() {
    document.getElementById('pause-resume-btn').style.display = 'none';
}














