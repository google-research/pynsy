from types import FrameType
import inspect

def get_instrumented_program_frame() -> FrameType:
  is_next_frame = False
  for frame_container in inspect.getouterframes(inspect.currentframe()):
    if is_next_frame:
      return frame_container.frame
    elif frame_container.function == "py_instrument_receiver":
      is_next_frame = True
  raise Exception("Frame in instrumented code not found")
