# MeetingTrack

MeetingTrack is a Python-based application designed to automate the generation of meeting transcripts and extraction of crucial insights and tasks from daily team meetings in offices. It leverages speech-to-text conversion and a language model to provide an efficient and convenient solution for teams.

## Track - LLM API Endpoint

## Problem Statement
- Lack of comprehensive software for tracking and analyzing Daily Team Meetings (DTMs).
- Challenges in enhancing collaboration and individual contributions without systematic DTM insights.
- Difficulty in identifying areas for improvement and tracing the origins of bugs.
- Inefficiency due to manual analysis of DTMs, leading to poor resource utilization.
- Limited capability to generate actionable insights and performance metrics from DTM discussions.
- Challenges in tracking meeting insights and providing timely feedback.

## Solution 
- Implemented routes and endpoints within the Flask-based API to handle audio processing, insights extraction, and summary generation.
- Integrated the DTM transcription module to convert audio recordings into text using the OpenAI Whisper API.
- Utilized the GPT API for natural language processing tasks and analysis.
- The API supports US-English, Spanish, and most Indic-Regional languages.
- Seamlessly integrates with team members' Google Calendars to automatically add notes and reminders based on extracted DTM insights.

## API ENDPOINTS
- [OpenAI GPT-4 API Documentation](https://platform.openai.com/docs/models/gpt-4o)
- [Google Calendar API Documentation](https://console.cloud.google.com/projectselector2/apis/library/calendar.googleapis.com?supportedpurview=project)

## Video Link
[Video Link](https://drive.google.com/file/d/1qVJH4OmA_uwoTRjPb5rrbPZoQzwuNF80/view?usp=sharing) 

## Workflow
1. User selects the preferred language.
2. User chooses the audio input source (Microphone or Audio Stream).
3. Audio is recorded and saved as a WAV file.
4. Speech-to-text conversion is performed using the selected language and OpenAI Whisper API.
5. The transcribed text is processed using the GPT API to extract insights, summaries, and action items.
6. The resulting text is sent to Google Calendar for event creation and notification.
7. Weekly analysis is enabled based on Google Calendar data.

## Tech Stack/ Methodology
- Python: For server-side development.
- Flask: For building the API server.
- OpenAI GPT API: For Natural Language Processing and Text Generation.
- Google Calendar API: For note creation and notifications.
- Whisper API: For speech-to-text conversion.
- JSON and RESTful API for data exchange.
- Git for version control and collaborative development.

## Use Cases:
- Automated transcription and analysis of DTMs.
- Improved productivity and efficiency in meeting discussions.
- Seamless integration with Google Calendar for event management.
- Multilingual support for enhanced user experience.

## USPs
- Real-time Transcription
- Multilingual Support
- Accurate Speech-to-Text Conversion
- Intelligent Meeting Highlights
- Google Calendar Integration
- Weekly Data Analysis
- Enhanced Efficiency

## Future Scope:
- Developing an Interactive Dashboard
- Voice Assistant Integration
- Enhanced Scalability
- Custom Analysis Periods

## Acknowledgments
This project is inspired by the need to automate and streamline the process of daily team meetings. We express our gratitude to the developers and contributors of the libraries and APIs used in this project, including the GPT API and Google Cloud services.
