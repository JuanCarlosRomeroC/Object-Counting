import matplotlib.pyplot as plt
import numpy as np

def plot_loss(train_loss, val_loss, title='loss'):
    x = np.arange(len(train_loss)) + 1
    
    plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    plt.title(title)
    plt.plot(x, train_loss, label='train')
    plt.plot(x, val_loss, label='val')
    plt.ylabel(title)
    plt.xlabel('epoch')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.title(f'Log({title})')
    plt.plot(x, np.log(train_loss), label='train')
    plt.plot(x, np.log(val_loss), label='val')
    plt.ylabel(f'Log({title})')
    plt.xlabel('epoch')
    plt.legend()
    
    plt.show()
    
def plot_some_predictions(images, density_maps, preds):
    num_images = len(images)
    for i in range(num_images):
        plt.figure(figsize=(15, 12))
        plt.subplot(num_images, 3, 1)
        plt.title('initial image')
        plt.imshow(images[i])
        
        vmin = min(density_maps[i].min(), preds[i].min())
        vmax = max(density_maps[i].max(), preds[i].max())
        
        plt.subplot(num_images, 3, 2)
        plt.title(f'gt density map: {density_maps[i].sum():.2f}')
        plt.imshow(density_maps[i], cmap='jet', vmin=vmin, vmax=vmax)
        plt.colorbar(fraction=0.045, pad=0.04)
        plt.axis('off')

        plt.subplot(num_images, 3, 3)
        pred = preds[i].squeeze()
        plt.title(f'pred density map: {pred.sum():.2f}')
        plt.imshow(pred, cmap='jet', vmin=vmin, vmax=vmax)
        plt.colorbar(fraction=0.045, pad=0.04)
        plt.axis('off')
        
def plot_gt_vs_pred_counts(gt_counts, pred_counts, split_name, new_figure=True):
    diff = gt_counts - pred_counts
    sorted_indices = np.argsort(diff)
    
    print()
    print(f'{split_name} set: {len(gt_counts)} images')
    print(f'Underestimation in {(diff > 0).sum()} images')
    print(f'Overestimation in {(diff < 0).sum()} images')
    
    if new_figure:
        plt.figure(figsize=(7.5, 5))
    plt.title(f'GT vs Predicted counts ({split_name} set: {len(gt_counts)} images)')
    plt.plot(gt_counts[sorted_indices], color='green', label='GT count')
    plt.plot(pred_counts[sorted_indices], label='Predicted count')
    plt.ylabel('count')
    plt.xlabel('images (asc order of count difference)')
    plt.legend()