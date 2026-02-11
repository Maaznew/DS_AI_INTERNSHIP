# task 1
import numpy as np
scores=np.random.randint(50,101, size=(5,3))
subject_means = scores.mean(axis=0)
centered_scores=scores-subject_means
print("original scores (student x score):")
print(scores)
print("\n mean of each subject:")
print(subject_means)
print("\ncenterd scores (after broadcasting):")
print(centered_scores)

#task 2

data=np.arange(24)
reshape_data=data.reshape(4,3,2)
final_data=reshape_data.transpose(0, 2, 1)
print("final shape:",final_data.shape)
print("final array:")
print(final_data)


