weight_loss_exercises = [
        {'name': 'Squats', 'duration': 30, 'video_url':'https://www.youtube.com/embed/rMvwVtlqjTE?si=8Kd99ihni_Eri4Ob;controls=0', 'start_time':7, 'end_time':37},
        {'name': 'Pushups', 'duration': 30, 'video_url': 'https://www.youtube.com/embed/_l3ySVKYVJ8?si=R0Ld3dTblJEr03oI;controls=0', 'start_time':0, 'end_time':30},
        {'name': 'Situps', 'duration': 30, 'video_url': 'https://www.youtube.com/embed/_HDZODOx7Zw?si=w5AzD4vSlKj9zhja;controls=0','start_time':0, 'end_time':30},
        {'name': 'Burpees', 'duration': 30, 'video_url':'https://www.youtube.com/embed/auBLPXO8Fww?si=DR6KYMtO1-8qIojQ;controls=0','start_time':0, 'end_time':30 },
        {'name': 'Mountain Climbers', 'duration': 30, 'video_url': 'https://youtu.be/kLh-uczlPLg?si=NoEYNULiKhK0KXL;controls=0', 'start_time':0, 'end_time':30},
        {'name': 'Lunge Jumps', 'duration': 30, 'video_url': 'https://www.youtube.com/embed/iJMsF7fzrOM?si=TWn2jsC6DF6YXk8c', 'start_time':0, 'end_time':16},
        {'name': 'Plank', 'duration': 60, 'video_url': 'https://www.youtube.com/embed/sZxrs3C209k?si=2Uo2QT83dF03zKoS&amp;controls=0', 'start_time':0, 'end_time':16},
        {'name': 'Punches non-stop', 'duration': 60, 'video_url': 'https://www.youtube.com/embed/8BPuS9uj5c8?si=VGCffZbNHqNUmSXM&amp;controls=0'},
]

tone_down_exercises = [
        {'name': 'Plank', 'duration': 60, 'video_url': 'https://www.youtube.com/embed/sZxrs3C209k?si=2Uo2QT83dF03zKoS&amp;controls=0', 'start_time':0, 'end_time':16},
        {'name': 'Glute Bridge', 'duration': 30, 'video_url':'https://www.youtube.com/embed/Xp33YgPZgns?si=oJP96xGUVvAWmDba&amp;controls=0', 'start_time':0, 'end_time':30},
        {'name': 'Jumping Jacks', 'duration': 60, 'video_url':'https://www.youtube.com/embed/PBHUfBzxczU?si=fPZdKm8ncoHfnr5e', 'start_time':0, 'end_time':4},
        {'name': 'Side Lunges', 'duration': 30, 'video_url':'https://www.youtube.com/embed/rvqLVxYqEvo?si=2UD1ozdmB4KGNAlY&amp;controls=0', 'start_time':15, 'end_time':45},
        {'name': 'Lunge Jumps', 'duration': 30, 'video_url': 'https://www.youtube.com/embed/iJMsF7fzrOM?si=TWn2jsC6DF6YXk8c', 'start_time':0, 'end_time':16},
        {'name': 'Squats', 'duration': 30, 'video_url':'https://www.youtube.com/embed/rMvwVtlqjTE?si=8Kd99ihni_Eri4Ob;controls=0', 'start_time':7, 'end_time':37},
        {'name': 'Squats', 'duration': 30, 'video_url':'https://www.youtube.com/embed/rMvwVtlqjTE?si=8Kd99ihni_Eri4Ob;controls=0', 'start_time':7, 'end_time':37},
]

build_muscle_exercises = [
        {'name': 'Pistol Squat', 'duration': 30, 'video_url':'https://www.youtube.com/embed/qDcniqddTeE?si=Bspe4SGoNtHRlpkx&amp;controls=0', 'start_time':0, 'end_time':30},
        {'name': 'Dips', 'duration': 30, 'video_url':'https://www.youtube.com/embed/HCf97NPYeGY?si=6JGCn39zlH0_VUFG&amp;controls=0', 'start_time':0, 'end_time':18},
        {'name': 'Situps', 'duration': 30, 'video_url': 'https://www.youtube.com/embed/_HDZODOx7Zw?si=w5AzD4vSlKj9zhja;controls=0','start_time':0, 'end_time':30},
        {'name': 'Burpees', 'duration': 30, 'video_url':'https://www.youtube.com/embed/auBLPXO8Fww?si=DR6KYMtO1-8qIojQ;controls=0','start_time':0, 'end_time':30 },
        {'name': 'Mountain Climbers', 'duration': 30, 'video_url': 'https://youtu.be/kLh-uczlPLg?si=NoEYNULiKhK0KXL;controls=0', 'start_time':0, 'end_time':30},
        {'name': 'Pushups', 'duration': 30, 'video_url': 'https://www.youtube.com/embed/_l3ySVKYVJ8?si=R0Ld3dTblJEr03oI;controls=0', 'start_time':0, 'end_time':30},
        {'name': 'Overhead Crunch', 'duration': 30, 'video_url':'https://www.youtube.com/embed/f02JON8c4J0?si=UVTjPYqemKsLQ91L&amp;controls=0', 'start_time':0, 'end_time':20},
        {'name': 'Plank', 'duration': 60, 'video_url': 'https://www.youtube.com/embed/sZxrs3C209k?si=2Uo2QT83dF03zKoS&amp;controls=0', 'start_time':0, 'end_time':16},
]

EXERCISES = {
    "loose-weight":{
        "exercise":weight_loss_exercises,
        "template":"fitness_jerk/exercise_loose.html"
    },
    "build-muscle":{
        "exercise":build_muscle_exercises,
        "template":"fitness_jerk/exercise_muscles.html",
    },
    "tone-down":{
        "exercise":tone_down_exercises,
        "template":"fitness_jerk/exercise_tone.html",
    }
}