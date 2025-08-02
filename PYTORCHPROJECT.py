import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
import cv2
import numpy as np
from PIL import Image
import os

# Step 1: CNN Model
class MaskClassifier(nn.Module):
    def __init__(self):
        super(MaskClassifier, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(16, 32, 3)
        self.fc1 = nn.Linear(32 * 23 * 23, 128)
        self.fc2 = nn.Linear(128, 2)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = x.view(-1, 32 * 23 * 23)
        x = torch.relu(self.fc1(x))
        return self.fc2(x)

# Step 2: Transform
transform = transforms.Compose([
    transforms.Resize((100, 100)),
    transforms.ToTensor()
])

# Step 3: Dataset loading
if not os.path.exists('dataset/with_mask'):
    print("Dataset not found. Please download and place in 'dataset/with_mask' and 'dataset/without_mask'")
    exit()

train_data = datasets.ImageFolder("dataset/", transform=transform)
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)

# Step 4: Train model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MaskClassifier().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

print("\nTraining model...\n")
for epoch in range(3):
    total_loss = 0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1} Loss: {total_loss/len(train_loader):.4f}")

# Step 5: Save model
torch.save(model.state_dict(), "mask_model.pth")
print("\nTraining complete. Saved model as mask_model.pth")

# Step 6: Real-time webcam detection
print("\nStarting webcam... Press 'q' to quit.\n")
model.eval()

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert BGR to RGB
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(img)
    img_tensor = transform(pil_img).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img_tensor)
        _, predicted = torch.max(output, 1)
        label = "Mask" if predicted.item() == 0 else "No Mask"

    # Show result
    cv2.putText(frame, label, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2,
                (0, 255, 0) if label == "Mask" else (0, 0, 255), 3)
    cv2.imshow("Mask Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
