FROM python:3.10
COPY . .
RUN pip3 install tkinter pyttsx3 os
CMD ["python3", "Text_to_Speech_Project.py"]
