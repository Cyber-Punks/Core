# Imports the Google Cloud client library
from google.cloud import language_v1
import sys

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = sys.argv[1]
document = language_v1.Document(content=text, type_=language_v1.Document.Type.PLAIN_TEXT)
# Available values: NONE, UTF8, UTF16, UTF32
encoding_type = language_v1.EncodingType.UTF8

# Detects the sentiment of the entire text (sentiment, magnitude)
sentiment = client.analyze_sentiment(request = {'document': document}).document_sentiment
magnitude = annotations.document_sentiment.magnitude

# Detects the syntax of the text
response = client.analyze_syntax(request = {'document': document, 'encoding_type': encoding_type})
# Loop through tokens returned from the API
for token in response.tokens:
    # Get the text content of this token. Usually a word or punctuation.
    text = token.text
    print(u"Token text: {}".format(text.content))
    print(
        u"Location of this token in overall document: {}".format(text.begin_offset)
    )
    # Get the part of speech information for this token.
    # Parts of spech are as defined in:
    # http://www.lrec-conf.org/proceedings/lrec2012/pdf/274_Paper.pdf
    part_of_speech = token.part_of_speech
    # Get the tag, e.g. NOUN, ADJ for Adjective, et al.
    print(
        u"Part of Speech tag: {}".format(
            language_v1.PartOfSpeech.Tag(part_of_speech.tag).name
        )
    )
    # Get the voice, e.g. ACTIVE or PASSIVE
    print(u"Voice: {}".format(language_v1.PartOfSpeech.Voice(part_of_speech.voice).name))
    # Get the tense, e.g. PAST, FUTURE, PRESENT, et al.
    print(u"Tense: {}".format(language_v1.PartOfSpeech.Tense(part_of_speech.tense).name))
    # See API reference for additional Part of Speech information available
    # Get the lemma of the token. Wikipedia lemma description
    # https://en.wikipedia.org/wiki/Lemma_(morphology)
    print(u"Lemma: {}".format(token.lemma))
    # Get the dependency tree parse information for this token.
    # For more information on dependency labels:
    # http://www.aclweb.org/anthology/P13-2017
    dependency_edge = token.dependency_edge
    print(u"Head token index: {}".format(dependency_edge.head_token_index))
    print(
        u"Label: {}".format(language_v1.DependencyEdge.Label(dependency_edge.label).name)
    )

# Get the language of the text, which will be the same as
# the language specified in the request or, if not specified,
# the automatically-detected language.
print(u"Language of the text: {}".format(response.language))
print("Text: {}".format(text))
print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))