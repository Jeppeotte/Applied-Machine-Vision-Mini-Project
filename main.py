# Import the InferencePipeline object
from inference import InferencePipeline
# Import the built in render_boxes sink for visualizing results
from inference.core.interfaces.stream.sinks import render_boxes

# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="crushedcansdetection/3", # Roboflow model to use
    video_reference=1, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=render_boxes, # Function to run after each prediction
    confidence=0.75, # Confidence
    api_key="Insert API KEY", # Insert own API key
)
pipeline.start()
pipeline.join()
