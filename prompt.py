class CustomPrompt:
    def __init__(self) -> None:
        self.prompt_text = """Be a skilled ATS(Aplication Tracking System) to read find and fetch all the similer kewards that matches with job description. As picking the most relevent resume is very competitive you should be carefully assign the percentence of match data between the job description and resume. Please also mention the missing keywords that are not present in the resume but job description require

        resume:{text}
        description:{job_description}

        my output structure should be consise and within just one line and following instruction bellow
        {{"Match Keywords:"%", Missing Keywords:[]}}"""