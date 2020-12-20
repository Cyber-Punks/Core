from google.cloud import language_v1
import sys

sentiment_threshold = -.7
magnitude_threshold = 5

def analyze_entity_sentiment(text_content):
    naughty = False

    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = language_v1.Document.Type.PLAIN_TEXT

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8
    document = {"content": text_content, "type_": type_}

    #Get the analysis of the individual entities (subjects) and overall sentiment respectively
    entity_analysis = client.analyze_entity_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    sentiment_analysis = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    overall_sentiment = sentiment_analysis.document_sentiment.score
    overal_magnitude = sentiment_analysis.document_sentiment.magnitude

    # Is the overall statement quite negative?
    if (overall_sentiment < sentiment_threshold and overal_magnitude > magnitude_threshold):
        naughty = True

    # Loop through entitites returned from the API
    subjects = []
    for entity in entity_analysis.entities:
        subject_json = {
            "name": entity.name,
            "score": entity.sentiment.score,
            "magnitude": entity.sentiment.magnitude
        }

        subjects.append(subject_json)

    response_json = {
        "naughty" : naughty,
        "subjects": subjects
    }

    print(response_json)
    
    return response_json

def main():
    analyze_entity_sentiment(sys.argv[1])

if __name__ == "__main__":
    main()