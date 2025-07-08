from openai import OpenAI

OPENAI_TOKEN = "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"
OPENAI_FILE_ID = "file-9KbXt8Xua3PfdDqeTF4R7b"
OPENAI_MODEL = "gpt-4.1-nano-2025-04-14"

client = OpenAI(api_key=OPENAI_TOKEN)

ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model=OPENAI_MODEL
)

# Notez absolument le modèle fine-tuné, il sera nécessaire pour l'utilisation du modèle fine-tuné
print("Fine Tune Job has been created with id ", ft_job.id)