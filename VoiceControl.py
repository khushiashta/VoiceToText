import speech_recognition as sr
import subprocess

def get_audio_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio_data).lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("There was a problem with the speech recognition service.")

def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print("Error executing command:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    while True:
        audio_input = get_audio_input()

        # Exit the loop if the user says 'exit'
        if audio_input == 'exit':
            print("Exiting...")
            break

        # Print the transcribed text
        print("You said:", audio_input)

        # Execute command if recognized as such
        if "run" in audio_input and "command" in audio_input:
            command = audio_input.replace("run", "").replace("command", "").strip()
            execute_command(command)
