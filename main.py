import openai


def wish(subject, occasion):
    """
    `wish` takes two arguments, `subject` and `occasion`, and returns a string that is a message wishing the subject a happy
    occasion

    :param subject: The person you want to wish
    :param occasion: The occasion for which you want to wish someone
    :return: A string
    """
    prompt = f"Write a message to wish {subject} happy {occasion}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,  # controls randomness
        max_tokens=64,  # 1 token = 4 characters
        top_p=1,  # controls diversity
        frequency_penalty=0,
        presence_penalty=0,
    )
    retVal = response.choices[0].text
    print(retVal)
    return retVal


if __name__ == "__main__":
    wish("Shyamal", "graduation")
