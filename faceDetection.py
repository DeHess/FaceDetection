from deepface import DeepFace

result = DeepFace.verify(
  img1_path = "gf1.jpg",
  img2_path = "gf2komma5.jpg",
)

print(str(result))