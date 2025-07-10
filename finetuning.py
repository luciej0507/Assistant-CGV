from openai import OpenAI

client = OpenAI(api_key=OPENAI_TOKEN)

ft_job = client.fine_tuning.jobs.create(
  training_file=OPENAI_FILE_ID,
  model=OPENAI_MODEL
)

# Notez absolument le modèle fine-tuné, il sera nécessaire pour l'utilisation du modèle fine-tuné
print("Fine Tune Job has been created with id ", ft_job.id)
