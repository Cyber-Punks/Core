from google.cloud import language_v1
import sys

# Thresholds for determining if a statement is too negative
sentiment_threshold = -0.7
magnitude_threshold = 0.7

# Input a string and output a dict/json sentiment analysis object
def analyze_entity_sentiment(text_content):
    client = language_v1.LanguageServiceClient()
    type_ = language_v1.Document.Type.PLAIN_TEXT
    encoding_type = language_v1.EncodingType.UTF8
    document = {"content": text_content, "type_": type_}

    #Get the analysis of the individual entities (subjects) and overall sentiment respectively
    entity_analysis = client.analyze_entity_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    sentiment_analysis = client.analyze_sentiment(request = {'document': document, 'encoding_type': encoding_type})
    overall_sentiment = sentiment_analysis.document_sentiment.score
    overal_magnitude = sentiment_analysis.document_sentiment.magnitude

    # Is the overall statement quite negative?
    naughty = False
    if (overall_sentiment < sentiment_threshold and overal_magnitude > magnitude_threshold):
        naughty = True

    # Loop through individual entitities(sentence subjects)
    # Add their scores to a list
    subjects = []
    for entity in entity_analysis.entities:
        subject_json = {
            "name": entity.name,
            "score": entity.sentiment.score,
            "magnitude": entity.sentiment.magnitude
        }

        subjects.append(subject_json)

    # Build the final dict to be returned
    response_json = {
        "naughty" : naughty,
        "subjects": subjects
    }

    return response_json

def main():
    analyze_entity_sentiment(sys.argv[1])

if __name__ == "__main__":
    main()
