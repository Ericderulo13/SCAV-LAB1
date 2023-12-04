# Use the official Ubuntu image as the base
FROM ubuntu:latest

# Update package lists and install FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Create a directory to hold your files (optional)
WORKDIR /app

# Copy the bbb5.mp4 file from the host machine to the Docker image
COPY bbb5.mp4 /app/bbb5.mp4

# Set the default command to run when the container starts
CMD ffmpeg -i bbb5.mp4 -filter_complex "[0:v]setpts=0.5*PTS[outv];[outv]eq=saturation=1.5:brightness=0.2:contrast=1.3,boxblur=10:5[outf];[0:a]atempo=2[outa]" -map "[outf]" -map "[outa]" output.mp4

